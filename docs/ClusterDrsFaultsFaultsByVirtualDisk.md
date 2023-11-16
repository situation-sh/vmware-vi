# ClusterDrsFaultsFaultsByVirtualDisk

The faults generated by storage DRS when it tries to move a virtual disk.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**VirtualDiskId**](VirtualDiskId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_drs_faults_faults_by_virtual_disk import ClusterDrsFaultsFaultsByVirtualDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDrsFaultsFaultsByVirtualDisk from a JSON string
cluster_drs_faults_faults_by_virtual_disk_instance = ClusterDrsFaultsFaultsByVirtualDisk.from_json(json)
# print the JSON string representation of the object
print ClusterDrsFaultsFaultsByVirtualDisk.to_json()

# convert the object into a dict
cluster_drs_faults_faults_by_virtual_disk_dict = cluster_drs_faults_faults_by_virtual_disk_instance.to_dict()
# create an instance of ClusterDrsFaultsFaultsByVirtualDisk from a dict
cluster_drs_faults_faults_by_virtual_disk_form_dict = cluster_drs_faults_faults_by_virtual_disk.from_dict(cluster_drs_faults_faults_by_virtual_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

