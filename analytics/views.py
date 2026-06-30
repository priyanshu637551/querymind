from django.shortcuts import render

from .forms import QueryForm
from .services.gemini_service import generate_sql, fix_sql
from .services.sql_executor import execute_sql
from .models import QueryLog
from .services.summary_generator import generate_summary
from .services.chart_generator import generate_chart
import json
from .services.dashboard_service import get_dashboard_stats
import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator



def home(request):
    result = None
    if request.method == "POST":
        question = request.POST.get("question")
        sql = ""
        summary = ""
        chart = ""
        columns = []
        rows = []
        try:
            sql = generate_sql(question)
            try:
                columns, rows = execute_sql(sql)
                chart = generate_chart(columns, rows)
                chart = chart or ""
            except Exception as e:
                fixed_sql = fix_sql(
                    question,
                    sql,
                    str(e)
                )
                columns, rows = execute_sql(fixed_sql)
                sql = fixed_sql

            summary = generate_summary(
                question,
                columns,
                rows
            )

            result_json = {
            "columns": columns,
            "rows": [[str(value) for value in row] for row in rows]
            }
            
            QueryLog.objects.create(
                question=question,
                generated_sql=sql,
                ai_summary=summary,
                chart_html=chart,
                result_json=result_json,
                status="Success"
            )
            result = {
                "question": question,
                "sql": sql,
                "columns": columns,
                "rows": rows,
                "summary": summary,
                "chart":chart
            }
        except Exception as e:

            if "429" in str(e):
                result = {
                "question": question,
                "sql": "Gemini free quota exhausted. Please try again later.",
                "columns": [],
                "rows": [],
                "summary": "",
                "chart": ""
                }

            else:
                result = {
                "question": question,
                "sql": f"Error: {e}",
                "columns": [],
                "rows": [],
                "summary": "",
                "chart": ""
                }
    dashboard = get_dashboard_stats()

    return render(request,"analytics/home.html",{
        "form": QueryForm(),
        "result": result,
        "dashboard": dashboard
        }
    )

def history(request):
    queries = QueryLog.objects.order_by("-created_at")
    search = request.GET.get("search")
    status = request.GET.get("status")

    if search:
        queries = queries.filter(question__icontains=search)

    if status:
        queries = queries.filter(status=status)

    paginator = Paginator(queries, 10)

    page_number = request.GET.get("page")

    queries = paginator.get_page(page_number)

    return render(
        request,
        "analytics/history.html",
        {
            "queries": queries,
            "search": search,
            "status": status,
        }
    )


def export_csv(request):
    latest = QueryLog.objects.order_by("-created_at").first()

    if not latest or not latest.result_json:
        return HttpResponse("No data available.")

    data = latest.result_json

    columns = data["columns"]
    rows = data["rows"]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="query_results.csv"'

    writer = csv.writer(response)

    writer.writerow(columns)

    for row in rows:
        writer.writerow(row)

    return response




def report_detail(request, pk):

    report = get_object_or_404(
        QueryLog,
        pk=pk
    )

    result_json = report.result_json or {}

    context = {
        "report": report,
        "columns": result_json.get("columns", []),
        "rows": result_json.get("rows", [])
    }

    return render(
        request,
        "analytics/report_detail.html",
        context
    )