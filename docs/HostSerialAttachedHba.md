# HostSerialAttachedHba

The data object type describes the Serial Attached Scsi(SAS) interface.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_world_wide_name** | **str** | The world wide node name for the adapter.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.host_serial_attached_hba import HostSerialAttachedHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostSerialAttachedHba from a JSON string
host_serial_attached_hba_instance = HostSerialAttachedHba.from_json(json)
# print the JSON string representation of the object
print HostSerialAttachedHba.to_json()

# convert the object into a dict
host_serial_attached_hba_dict = host_serial_attached_hba_instance.to_dict()
# create an instance of HostSerialAttachedHba from a dict
host_serial_attached_hba_form_dict = host_serial_attached_hba.from_dict(host_serial_attached_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


