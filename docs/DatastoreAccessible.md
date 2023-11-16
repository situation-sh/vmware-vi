# DatastoreAccessible

A boxed *DatastoreAccessible_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DatastoreAccessibleEnum**](DatastoreAccessibleEnum.md) |  | 

## Example

```python
from vmware_vi.models.datastore_accessible import DatastoreAccessible

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreAccessible from a JSON string
datastore_accessible_instance = DatastoreAccessible.from_json(json)
# print the JSON string representation of the object
print DatastoreAccessible.to_json()

# convert the object into a dict
datastore_accessible_dict = datastore_accessible_instance.to_dict()
# create an instance of DatastoreAccessible from a dict
datastore_accessible_form_dict = datastore_accessible.from_dict(datastore_accessible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


