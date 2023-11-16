# NoConnectedDatastore

The fault occurs when Storage DRS cannot move a virtual machine because the host it is registered on is not connected to any other datastore in the storage pod.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_connected_datastore import NoConnectedDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of NoConnectedDatastore from a JSON string
no_connected_datastore_instance = NoConnectedDatastore.from_json(json)
# print the JSON string representation of the object
print NoConnectedDatastore.to_json()

# convert the object into a dict
no_connected_datastore_dict = no_connected_datastore_instance.to_dict()
# create an instance of NoConnectedDatastore from a dict
no_connected_datastore_form_dict = no_connected_datastore.from_dict(no_connected_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


