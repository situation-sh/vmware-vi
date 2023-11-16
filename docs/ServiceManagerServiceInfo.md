# ServiceManagerServiceInfo

This data object represents essential information about a particular service.  The information is sufficient to be able to identify the service and retrieve the object implementing it. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** | A service name.  Each service is expected to create a unique name for itself that can be used to locate the service. This name does not need to be unique across hosts or other such locations though.  | 
**location** | **List[str]** | A list of data that can be used to uniquely identify a particular instance of a service.  Multiple instances of a service can exist across different domains (for instance, a service that is associated with a particular virtual machine or a particular host). In such cases, the service name is insufficient to identify the service and location data can be used to identify the instance of interest. A service may publish as much location data as is needed to identify it (e.g, vmware.host.&amp;lt;hostname&amp;gt; or vmware.vm.&amp;lt;uuid&amp;gt; or both). The particular choice of locations have to be agreed upon by the client and the service.  | [optional] 
**service** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**description** | **str** | A description of the service.  Provides help text on how to use the service.  | 

## Example

```python
from vmware_vi.models.service_manager_service_info import ServiceManagerServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManagerServiceInfo from a JSON string
service_manager_service_info_instance = ServiceManagerServiceInfo.from_json(json)
# print the JSON string representation of the object
print ServiceManagerServiceInfo.to_json()

# convert the object into a dict
service_manager_service_info_dict = service_manager_service_info_instance.to_dict()
# create an instance of ServiceManagerServiceInfo from a dict
service_manager_service_info_form_dict = service_manager_service_info.from_dict(service_manager_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


