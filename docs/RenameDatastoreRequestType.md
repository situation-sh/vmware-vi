# RenameDatastoreRequestType

The parameters of *Datastore.RenameDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** | The new name to assign to the datastore.  | 

## Example

```python
from vmware_vi.models.rename_datastore_request_type import RenameDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RenameDatastoreRequestType from a JSON string
rename_datastore_request_type_instance = RenameDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print RenameDatastoreRequestType.to_json()

# convert the object into a dict
rename_datastore_request_type_dict = rename_datastore_request_type_instance.to_dict()
# create an instance of RenameDatastoreRequestType from a dict
rename_datastore_request_type_form_dict = rename_datastore_request_type.from_dict(rename_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


