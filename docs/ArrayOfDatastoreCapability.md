# ArrayOfDatastoreCapability

A boxed array of *DatastoreCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreCapability]**](DatastoreCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_capability import ArrayOfDatastoreCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreCapability from a JSON string
array_of_datastore_capability_instance = ArrayOfDatastoreCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreCapability.to_json()

# convert the object into a dict
array_of_datastore_capability_dict = array_of_datastore_capability_instance.to_dict()
# create an instance of ArrayOfDatastoreCapability from a dict
array_of_datastore_capability_form_dict = array_of_datastore_capability.from_dict(array_of_datastore_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


