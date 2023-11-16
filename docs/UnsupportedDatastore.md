# UnsupportedDatastore

The virtual machine is not supported on the target datastore.  This fault is thrown by provisioning operations when an attempt is made to create a virtual machine on an unsupported datastore (for example, creating a non-legacy virtual machine on a legacy datastore). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.unsupported_datastore import UnsupportedDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of UnsupportedDatastore from a JSON string
unsupported_datastore_instance = UnsupportedDatastore.from_json(json)
# print the JSON string representation of the object
print UnsupportedDatastore.to_json()

# convert the object into a dict
unsupported_datastore_dict = unsupported_datastore_instance.to_dict()
# create an instance of UnsupportedDatastore from a dict
unsupported_datastore_form_dict = unsupported_datastore.from_dict(unsupported_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


