# UpdateVVolVirtualMachineFilesRequestType

The parameters of *Datastore.UpdateVVolVirtualMachineFiles_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_pair** | [**List[DatastoreVVolContainerFailoverPair]**](DatastoreVVolContainerFailoverPair.md) | Mapping of source to target storage container as well as source to target VVol IDs.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.update_v_vol_virtual_machine_files_request_type import UpdateVVolVirtualMachineFilesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVVolVirtualMachineFilesRequestType from a JSON string
update_v_vol_virtual_machine_files_request_type_instance = UpdateVVolVirtualMachineFilesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVVolVirtualMachineFilesRequestType.to_json()

# convert the object into a dict
update_v_vol_virtual_machine_files_request_type_dict = update_v_vol_virtual_machine_files_request_type_instance.to_dict()
# create an instance of UpdateVVolVirtualMachineFilesRequestType from a dict
update_v_vol_virtual_machine_files_request_type_form_dict = update_v_vol_virtual_machine_files_request_type.from_dict(update_v_vol_virtual_machine_files_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


