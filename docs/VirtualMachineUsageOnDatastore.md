# VirtualMachineUsageOnDatastore

Storage space used by this virtual machine on a particular datastore.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**committed** | **int** | Storage space, in bytes, on this datastore that is actually being used by the virtual machine.  It includes space actually occupied by disks, logs, snapshots, configuration files etc. Files of the virtual machine which are present on a different datastore (e.g. a virtual disk on another datastore) are not included here. *VirtualMachineFileLayoutEx* provides a detailed break-up of the committed space.  ***Since:*** vSphere API 4.0  | 
**uncommitted** | **int** | Additional storage space, in bytes, potentially used by the virtual machine on this datastore.  Additional space may be needed for example when lazily allocated disks grow, or storage for swap is allocated when powering on the virtual machine.  If the virtual machine is running off delta disks (for example because a snapshot was taken), then only the potential growth of the currently used delta-disks is considered.  ***Since:*** vSphere API 4.0  | 
**unshared** | **int** | Storage space, in bytes, occupied by the virtual machine on this datastore that is not shared with any other virtual machine.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_usage_on_datastore import VirtualMachineUsageOnDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineUsageOnDatastore from a JSON string
virtual_machine_usage_on_datastore_instance = VirtualMachineUsageOnDatastore.from_json(json)
# print the JSON string representation of the object
print VirtualMachineUsageOnDatastore.to_json()

# convert the object into a dict
virtual_machine_usage_on_datastore_dict = virtual_machine_usage_on_datastore_instance.to_dict()
# create an instance of VirtualMachineUsageOnDatastore from a dict
virtual_machine_usage_on_datastore_form_dict = virtual_machine_usage_on_datastore.from_dict(virtual_machine_usage_on_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


