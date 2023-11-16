# AddFilterEntitiesRequestType

The parameters of *HealthUpdateManager.AddFilterEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | The filter id.  | 
**entities** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of additional managed entities. Only entities of type HostSystem or ClusterComputeResource are valid.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.add_filter_entities_request_type import AddFilterEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddFilterEntitiesRequestType from a JSON string
add_filter_entities_request_type_instance = AddFilterEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print AddFilterEntitiesRequestType.to_json()

# convert the object into a dict
add_filter_entities_request_type_dict = add_filter_entities_request_type_instance.to_dict()
# create an instance of AddFilterEntitiesRequestType from a dict
add_filter_entities_request_type_form_dict = add_filter_entities_request_type.from_dict(add_filter_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


