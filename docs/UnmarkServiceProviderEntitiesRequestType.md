# UnmarkServiceProviderEntitiesRequestType

The parameters of *TenantTenantManager.UnmarkServiceProviderEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | an array of management entities.  ***Required privileges:*** TenantManager.Update  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.unmark_service_provider_entities_request_type import UnmarkServiceProviderEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmarkServiceProviderEntitiesRequestType from a JSON string
unmark_service_provider_entities_request_type_instance = UnmarkServiceProviderEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print UnmarkServiceProviderEntitiesRequestType.to_json()

# convert the object into a dict
unmark_service_provider_entities_request_type_dict = unmark_service_provider_entities_request_type_instance.to_dict()
# create an instance of UnmarkServiceProviderEntitiesRequestType from a dict
unmark_service_provider_entities_request_type_form_dict = unmark_service_provider_entities_request_type.from_dict(unmark_service_provider_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


