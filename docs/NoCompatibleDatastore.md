# NoCompatibleDatastore

A NoCompatibleDatastore fault is thrown when Storage DRS cannot find a compatible datastore in a given storage pod to place a disk or a virtual machine.  a virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_compatible_datastore import NoCompatibleDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of NoCompatibleDatastore from a JSON string
no_compatible_datastore_instance = NoCompatibleDatastore.from_json(json)
# print the JSON string representation of the object
print NoCompatibleDatastore.to_json()

# convert the object into a dict
no_compatible_datastore_dict = no_compatible_datastore_instance.to_dict()
# create an instance of NoCompatibleDatastore from a dict
no_compatible_datastore_form_dict = no_compatible_datastore.from_dict(no_compatible_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


