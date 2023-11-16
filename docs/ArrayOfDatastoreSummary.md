# ArrayOfDatastoreSummary

A boxed array of *DatastoreSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreSummary]**](DatastoreSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_summary import ArrayOfDatastoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreSummary from a JSON string
array_of_datastore_summary_instance = ArrayOfDatastoreSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreSummary.to_json()

# convert the object into a dict
array_of_datastore_summary_dict = array_of_datastore_summary_instance.to_dict()
# create an instance of ArrayOfDatastoreSummary from a dict
array_of_datastore_summary_form_dict = array_of_datastore_summary.from_dict(array_of_datastore_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


