# DisallowedChangeByService

Fault thrown if the disallowed operation is invoked by the client.  The change is disallowed because it conflicts with target state maintained by a service. The corresponding method is usually not disabled because only a subset of changes carried out by the method is disallowed. For example, an online extend executed via virtual machine reconfigure method is not allowed if replication is enabled on a virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** | The service that has disallowed the change.  ***Since:*** vSphere API 5.0  | 
**disallowed_change** | **str** | The change this is not allowed, the set of possible values is described in *DisallowedChangeByServiceDisallowedChange_enum*.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.disallowed_change_by_service import DisallowedChangeByService

# TODO update the JSON string below
json = "{}"
# create an instance of DisallowedChangeByService from a JSON string
disallowed_change_by_service_instance = DisallowedChangeByService.from_json(json)
# print the JSON string representation of the object
print DisallowedChangeByService.to_json()

# convert the object into a dict
disallowed_change_by_service_dict = disallowed_change_by_service_instance.to_dict()
# create an instance of DisallowedChangeByService from a dict
disallowed_change_by_service_form_dict = disallowed_change_by_service.from_dict(disallowed_change_by_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


