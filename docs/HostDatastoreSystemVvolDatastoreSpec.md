# HostDatastoreSystemVvolDatastoreSpec

Specification for creating Virtual Volumed based datastore.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the datastore.  ***Since:*** vSphere API 6.0  | 
**sc_id** | **str** | Storage contained Id.  This is used to retrieve configuration of the storage container from SMS.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_datastore_system_vvol_datastore_spec import HostDatastoreSystemVvolDatastoreSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreSystemVvolDatastoreSpec from a JSON string
host_datastore_system_vvol_datastore_spec_instance = HostDatastoreSystemVvolDatastoreSpec.from_json(json)
# print the JSON string representation of the object
print HostDatastoreSystemVvolDatastoreSpec.to_json()

# convert the object into a dict
host_datastore_system_vvol_datastore_spec_dict = host_datastore_system_vvol_datastore_spec_instance.to_dict()
# create an instance of HostDatastoreSystemVvolDatastoreSpec from a dict
host_datastore_system_vvol_datastore_spec_form_dict = host_datastore_system_vvol_datastore_spec.from_dict(host_datastore_system_vvol_datastore_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


