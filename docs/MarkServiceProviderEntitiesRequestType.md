# MarkServiceProviderEntitiesRequestType

The parameters of *TenantTenantManager.MarkServiceProviderEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | an array of management entities.  ***Required privileges:*** TenantManager.Update  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.mark_service_provider_entities_request_type import MarkServiceProviderEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkServiceProviderEntitiesRequestType from a JSON string
mark_service_provider_entities_request_type_instance = MarkServiceProviderEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print MarkServiceProviderEntitiesRequestType.to_json()

# convert the object into a dict
mark_service_provider_entities_request_type_dict = mark_service_provider_entities_request_type_instance.to_dict()
# create an instance of MarkServiceProviderEntitiesRequestType from a dict
mark_service_provider_entities_request_type_form_dict = mark_service_provider_entities_request_type.from_dict(mark_service_provider_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


