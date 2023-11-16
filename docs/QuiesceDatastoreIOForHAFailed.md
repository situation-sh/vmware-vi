# QuiesceDatastoreIOForHAFailed

A QuiesceDatastoreIOForHAFailed fault occurs when the HA agent on a host cannot quiesce file activity on a datastore to be unmouonted or removed.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host_name** | **str** | Name of the host.  ***Since:*** vSphere API 5.0  | 
**ds** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**ds_name** | **str** | Name of the datastore.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.quiesce_datastore_io_for_ha_failed import QuiesceDatastoreIOForHAFailed

# TODO update the JSON string below
json = "{}"
# create an instance of QuiesceDatastoreIOForHAFailed from a JSON string
quiesce_datastore_io_for_ha_failed_instance = QuiesceDatastoreIOForHAFailed.from_json(json)
# print the JSON string representation of the object
print QuiesceDatastoreIOForHAFailed.to_json()

# convert the object into a dict
quiesce_datastore_io_for_ha_failed_dict = quiesce_datastore_io_for_ha_failed_instance.to_dict()
# create an instance of QuiesceDatastoreIOForHAFailed from a dict
quiesce_datastore_io_for_ha_failed_form_dict = quiesce_datastore_io_for_ha_failed.from_dict(quiesce_datastore_io_for_ha_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


