# ArrayOfDatastoreOption

A boxed array of *DatastoreOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreOption]**](DatastoreOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_option import ArrayOfDatastoreOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreOption from a JSON string
array_of_datastore_option_instance = ArrayOfDatastoreOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreOption.to_json()

# convert the object into a dict
array_of_datastore_option_dict = array_of_datastore_option_instance.to_dict()
# create an instance of ArrayOfDatastoreOption from a dict
array_of_datastore_option_form_dict = array_of_datastore_option.from_dict(array_of_datastore_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


