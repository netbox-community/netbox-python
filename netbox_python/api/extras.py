from netbox_python.baseapi import APIResource


class extras:
    def __init__(self, client):
        self.config_contexts = self._config_contexts(client)
        self.config_templates = self._config_templates(client)
        self.content_types = self._content_types(client)
        self.custom_fields = self._custom_fields(client)
        self.custom_links = self._custom_links(client)
        self.export_templates = self._export_templates(client)
        self.image_attachments = self._image_attachments(client)
        self.job_results = self._job_results(client)
        self.journal_entries = self._journal_entries(client)
        self.object_changes = self._object_changes(client)
        self.reports = self._reports(client)
        self.saved_filters = self._saved_filters(client)
        self.scripts = self._scripts(client)
        self.tags = self._tags(client)
        self.webhooks = self._webhooks(client)
        super().__init__()

    class _config_contexts(APIResource):
        path = "extras/config-contexts/"

    class _config_templates(APIResource):
        path = "extras/config-templates/"

    class _content_types(APIResource):
        path = "extras/content-types/"

    class _custom_fields(APIResource):
        path = "extras/custom-fields/"

    class _custom_links(APIResource):
        path = "extras/custom-links/"

    class _export_templates(APIResource):
        path = "extras/export-templates/"

    class _image_attachments(APIResource):
        path = "extras/image-attachments/"

    class _job_results(APIResource):
        path = "extras/job-results/"

    class _journal_entries(APIResource):
        path = "extras/journal-entries/"

    class _object_changes(APIResource):
        path = "extras/object-changes/"

    class _reports(APIResource):
        path = "extras/reports/"

    class _saved_filters(APIResource):
        path = "extras/saved-filters/"

    class _scripts(APIResource):
        path = "extras/scripts/"

    class _tags(APIResource):
        path = "extras/tags/"

    class _webhooks(APIResource):
        path = "extras/webhooks/"
