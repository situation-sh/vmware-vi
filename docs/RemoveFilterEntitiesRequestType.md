# RemoveFilterEntitiesRequestType

The parameters of *HealthUpdateManager.RemoveFilterEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | The filter id.  | 
**entities** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of removed managed entities.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.remove_filter_entities_request_type import RemoveFilterEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFilterEntitiesRequestType from a JSON string
remove_filter_entities_request_type_instance = RemoveFilterEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveFilterEntitiesRequestType.to_json()

# convert the object into a dict
remove_filter_entities_request_type_dict = remove_filter_entities_request_type_instance.to_dict()
# create an instance of RemoveFilterEntitiesRequestType from a dict
remove_filter_entities_request_type_form_dict = remove_filter_entities_request_type.from_dict(remove_filter_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


