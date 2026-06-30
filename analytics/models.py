from django.db import models


class QueryLog(models.Model):
    question = models.TextField()
    generated_sql = models.TextField()
    ai_summary = models.TextField(blank=True)
    chart_html = models.TextField(blank=True)
    result_json = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]