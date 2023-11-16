# HostParallelScsiHba

The ParallelScsiHba data object type describes a parallel SCSI host bus adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_parallel_scsi_hba import HostParallelScsiHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostParallelScsiHba from a JSON string
host_parallel_scsi_hba_instance = HostParallelScsiHba.from_json(json)
# print the JSON string representation of the object
print HostParallelScsiHba.to_json()

# convert the object into a dict
host_parallel_scsi_hba_dict = host_parallel_scsi_hba_instance.to_dict()
# create an instance of HostParallelScsiHba from a dict
host_parallel_scsi_hba_form_dict = host_parallel_scsi_hba.from_dict(host_parallel_scsi_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


