# ArrayOfPMemDatastoreInfo

A boxed array of *PMemDatastoreInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PMemDatastoreInfo]**](PMemDatastoreInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_p_mem_datastore_info import ArrayOfPMemDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPMemDatastoreInfo from a JSON string
array_of_p_mem_datastore_info_instance = ArrayOfPMemDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfPMemDatastoreInfo.to_json()

# convert the object into a dict
array_of_p_mem_datastore_info_dict = array_of_p_mem_datastore_info_instance.to_dict()
# create an instance of ArrayOfPMemDatastoreInfo from a dict
array_of_p_mem_datastore_info_form_dict = array_of_p_mem_datastore_info.from_dict(array_of_p_mem_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


