# UpdateVirtualMachineFilesRequestType

The parameters of *Datastore.UpdateVirtualMachineFiles_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path_datastore_mapping** | [**List[DatastoreMountPathDatastorePair]**](DatastoreMountPathDatastorePair.md) | Old mount path to datastore mapping.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.update_virtual_machine_files_request_type import UpdateVirtualMachineFilesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVirtualMachineFilesRequestType from a JSON string
update_virtual_machine_files_request_type_instance = UpdateVirtualMachineFilesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVirtualMachineFilesRequestType.to_json()

# convert the object into a dict
update_virtual_machine_files_request_type_dict = update_virtual_machine_files_request_type_instance.to_dict()
# create an instance of UpdateVirtualMachineFilesRequestType from a dict
update_virtual_machine_files_request_type_form_dict = update_virtual_machine_files_request_type.from_dict(update_virtual_machine_files_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


