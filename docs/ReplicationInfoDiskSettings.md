# ReplicationInfoDiskSettings

The ReplicationConfigSpec.DiskSettings object type encapsulates the replication properties of a replicated disk of a replicated virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | The disk&#39;s device key in the VM&#39;s configuration.  Used to uniquely identify the disk to be configured for replication in the primary VM.  ***Since:*** vSphere API 5.0  | 
**disk_replication_id** | **str** | An opaque identifier that uniquely identifies a replicated disk between primary and secondary sites.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.replication_info_disk_settings import ReplicationInfoDiskSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationInfoDiskSettings from a JSON string
replication_info_disk_settings_instance = ReplicationInfoDiskSettings.from_json(json)
# print the JSON string representation of the object
print ReplicationInfoDiskSettings.to_json()

# convert the object into a dict
replication_info_disk_settings_dict = replication_info_disk_settings_instance.to_dict()
# create an instance of ReplicationInfoDiskSettings from a dict
replication_info_disk_settings_form_dict = replication_info_disk_settings.from_dict(replication_info_disk_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


