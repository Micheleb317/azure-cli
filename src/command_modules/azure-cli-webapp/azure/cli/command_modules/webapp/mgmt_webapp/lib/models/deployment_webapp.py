#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentWebapp(Model):
    """
    Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateWebapp_2016-06-22/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :ivar _artifacts_location: Container URI of of the template. Default
     value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateWebapp_2016-06-22"
     .
    :vartype _artifacts_location: str
    :param hosting_plan: Name or ID of the web application's hosting plan.
    :type hosting_plan: str
    :param hosting_plan_type: Use a new or existing hosting plan. Possible
     values include: 'new', 'existingName', 'existingId'. Default value:
     "new" .
    :type hosting_plan_type: str
    :param name: Name for the web application.
    :type name: str
    :param number_of_workers: Number of dedicated VMs in the farm. Default
     value: "1" .
    :type number_of_workers: str
    :param sku_capacity: Describes plan's instance count. Default value: "1" .
    :type sku_capacity: str
    :param sku_name: Describes plan's pricing tier and instance size. Check
     details at
     https://azure.microsoft.com/en-us/pricing/details/app-service/. Default
     value: "F1" .
    :type sku_name: str
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        '_artifacts_location': {'required': True, 'constant': True},
        'name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        '_artifacts_location': {'key': 'properties.parameters._artifactsLocation.value', 'type': 'str'},
        'hosting_plan': {'key': 'properties.parameters.hostingPlan.value', 'type': 'str'},
        'hosting_plan_type': {'key': 'properties.parameters.hostingPlanType.value', 'type': 'str'},
        'name': {'key': 'properties.parameters.name.value', 'type': 'str'},
        'number_of_workers': {'key': 'properties.parameters.numberOfWorkers.value', 'type': 'str'},
        'sku_capacity': {'key': 'properties.parameters.skuCapacity.value', 'type': 'str'},
        'sku_name': {'key': 'properties.parameters.skuName.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateWebapp_2016-06-22/azuredeploy.json"

    _artifacts_location = "https://azuresdkci.blob.core.windows.net/templatehost/CreateWebapp_2016-06-22"

    mode = "Incremental"

    def __init__(self, name, content_version=None, hosting_plan=None, hosting_plan_type="new", number_of_workers="1", sku_capacity="1", sku_name="F1"):
        self.content_version = content_version
        self.hosting_plan = hosting_plan
        self.hosting_plan_type = hosting_plan_type
        self.name = name
        self.number_of_workers = number_of_workers
        self.sku_capacity = sku_capacity
        self.sku_name = sku_name