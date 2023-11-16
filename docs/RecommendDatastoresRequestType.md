# RecommendDatastoresRequestType

The parameters of *StorageResourceManager.RecommendDatastores*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_spec** | [**StoragePlacementSpec**](StoragePlacementSpec.md) |  | 

## Example

```python
from vmware_vi.models.recommend_datastores_request_type import RecommendDatastoresRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendDatastoresRequestType from a JSON string
recommend_datastores_request_type_instance = RecommendDatastoresRequestType.from_json(json)
# print the JSON string representation of the object
print RecommendDatastoresRequestType.to_json()

# convert the object into a dict
recommend_datastores_request_type_dict = recommend_datastores_request_type_instance.to_dict()
# create an instance of RecommendDatastoresRequestType from a dict
recommend_datastores_request_type_form_dict = recommend_datastores_request_type.from_dict(recommend_datastores_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


