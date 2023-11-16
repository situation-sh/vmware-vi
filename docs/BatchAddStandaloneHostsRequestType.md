# BatchAddStandaloneHostsRequestType

The parameters of *Folder.BatchAddStandaloneHosts_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_hosts** | [**List[FolderNewHostSpec]**](FolderNewHostSpec.md) | Specifies a list of host specifications for new hosts.  ***Since:*** vSphere API 6.7.1  | [optional] 
**comp_res_spec** | [**ComputeResourceConfigSpec**](ComputeResourceConfigSpec.md) |  | [optional] 
**add_connected** | **bool** | Flag to specify whether or not hosts should be connected at the time they are added. A host will not be added if a connection attempt is made and fails.  | 

## Example

```python
from vmware_vi.models.batch_add_standalone_hosts_request_type import BatchAddStandaloneHostsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAddStandaloneHostsRequestType from a JSON string
batch_add_standalone_hosts_request_type_instance = BatchAddStandaloneHostsRequestType.from_json(json)
# print the JSON string representation of the object
print BatchAddStandaloneHostsRequestType.to_json()

# convert the object into a dict
batch_add_standalone_hosts_request_type_dict = batch_add_standalone_hosts_request_type_instance.to_dict()
# create an instance of BatchAddStandaloneHostsRequestType from a dict
batch_add_standalone_hosts_request_type_form_dict = batch_add_standalone_hosts_request_type.from_dict(batch_add_standalone_hosts_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


