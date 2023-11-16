# IORMNotSupportedHostOnDatastore

A IORMNotSupportedHostOnDatastore fault occurs when the datastore is connected to one or more hosts that do not support storage I/O resource management.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**datastore_name** | **str** | The name of the datastore.  ***Since:*** vSphere API 4.1  | 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of hosts that do not support storage I/O resource management.  ***Since:*** vSphere API 4.1  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.iorm_not_supported_host_on_datastore import IORMNotSupportedHostOnDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of IORMNotSupportedHostOnDatastore from a JSON string
iorm_not_supported_host_on_datastore_instance = IORMNotSupportedHostOnDatastore.from_json(json)
# print the JSON string representation of the object
print IORMNotSupportedHostOnDatastore.to_json()

# convert the object into a dict
iorm_not_supported_host_on_datastore_dict = iorm_not_supported_host_on_datastore_instance.to_dict()
# create an instance of IORMNotSupportedHostOnDatastore from a dict
iorm_not_supported_host_on_datastore_form_dict = iorm_not_supported_host_on_datastore.from_dict(iorm_not_supported_host_on_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


