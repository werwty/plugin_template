"""
Check `Plugin Writer's Guide`_ for more details.

.. _Plugin Writer's Guide:
    http://docs.pulpproject.org/en/3.0/nightly/plugins/plugin-writer/index.html
"""
from rest_framework import serializers
from pulpcore.plugin import serializers as platform

from . import models


class PluginTemplateContentSerializer(platform.ContentSerializer):
    """
    A Serializer for PluginTemplateContent.

    Add serializers for the new fields defined in PluginTemplateContent and
    add those fields to the Meta class keeping fields from the parent class as well.

    For example::

    field1 = serializers.TextField()
    field2 = serializers.IntegerField()
    field3 = serializers.CharField()

    class Meta:
        fields = platform.ContentSerializer.Meta.fields + ('field1', 'field2', 'field3')
        model = models.PluginTemplateContent
    """

    class Meta:
        fields = platform.ContentSerializer.Meta.fields
        model = models.PluginTemplateContent


class PluginTemplateRemoteSerializer(platform.RemoteSerializer):
    """
    A Serializer for PluginTemplateRemote.

    Add any new fields if defined on PluginTemplateRemote.
    Similar to the example above, in PluginTemplateContentSerializer.
    Additional validators can be added to the parent validators list

    For example::

    class Meta:
        validators = platform.RemoteSerializer.Meta.validators + [myValidator1, myValidator2]
    """

    class Meta:
        fields = platform.RemoteSerializer.Meta.fields
        model = models.PluginTemplateRemote


class PluginTemplatePublisherSerializer(platform.PublisherSerializer):
    """
    A Serializer for PluginTemplatePublisher.

    Add any new fields if defined on PluginTemplatePublisher.
    Similar to the example above, in PluginTemplateContentSerializer.
    Additional validators can be added to the parent validators list

    For example::

    class Meta:
        validators = platform.PublisherSerializer.Meta.validators + [myValidator1, myValidator2]
    """

    class Meta:
        fields = platform.PublisherSerializer.Meta.fields
        model = models.PluginTemplatePublisher
