# ArrayOfClusterDrsFaultsFaultsByVirtualDisk

A boxed array of *ClusterDrsFaultsFaultsByVirtualDisk*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDrsFaultsFaultsByVirtualDisk]**](ClusterDrsFaultsFaultsByVirtualDisk.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_drs_faults_faults_by_virtual_disk import ArrayOfClusterDrsFaultsFaultsByVirtualDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDrsFaultsFaultsByVirtualDisk from a JSON string
array_of_cluster_drs_faults_faults_by_virtual_disk_instance = ArrayOfClusterDrsFaultsFaultsByVirtualDisk.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDrsFaultsFaultsByVirtualDisk.to_json()

# convert the object into a dict
array_of_cluster_drs_faults_faults_by_virtual_disk_dict = array_of_cluster_drs_faults_faults_by_virtual_disk_instance.to_dict()
# create an instance of ArrayOfClusterDrsFaultsFaultsByVirtualDisk from a dict
array_of_cluster_drs_faults_faults_by_virtual_disk_form_dict = array_of_cluster_drs_faults_faults_by_virtual_disk.from_dict(array_of_cluster_drs_faults_faults_by_virtual_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


