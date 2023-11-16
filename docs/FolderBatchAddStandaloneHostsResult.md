# FolderBatchAddStandaloneHostsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of hosts that were successfully added as standalone hosts to the inventory.  ***Since:*** vSphere API 6.7.1  Refers instances of *HostSystem*.  | [optional] 
**hosts_failed_inventory_add** | [**List[FolderFailedHostResult]**](FolderFailedHostResult.md) | Contains a fault for each host that failed to add.  A failed host will not be part of addedHosts list.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.folder_batch_add_standalone_hosts_result import FolderBatchAddStandaloneHostsResult

# TODO update the JSON string below
json = "{}"
# create an instance of FolderBatchAddStandaloneHostsResult from a JSON string
folder_batch_add_standalone_hosts_result_instance = FolderBatchAddStandaloneHostsResult.from_json(json)
# print the JSON string representation of the object
print FolderBatchAddStandaloneHostsResult.to_json()

# convert the object into a dict
folder_batch_add_standalone_hosts_result_dict = folder_batch_add_standalone_hosts_result_instance.to_dict()
# create an instance of FolderBatchAddStandaloneHostsResult from a dict
folder_batch_add_standalone_hosts_result_form_dict = folder_batch_add_standalone_hosts_result.from_dict(folder_batch_add_standalone_hosts_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


