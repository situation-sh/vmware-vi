# RemoveDatastoreExRequestType

The parameters of *HostDatastoreSystem.RemoveDatastoreEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | each element specifies one datastore to be removed.  Refers instances of *Datastore*.  | 

## Example

```python
from vmware_vi.models.remove_datastore_ex_request_type import RemoveDatastoreExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveDatastoreExRequestType from a JSON string
remove_datastore_ex_request_type_instance = RemoveDatastoreExRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveDatastoreExRequestType.to_json()

# convert the object into a dict
remove_datastore_ex_request_type_dict = remove_datastore_ex_request_type_instance.to_dict()
# create an instance of RemoveDatastoreExRequestType from a dict
remove_datastore_ex_request_type_form_dict = remove_datastore_ex_request_type.from_dict(remove_datastore_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


