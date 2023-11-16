# VmAlreadyExistsInDatacenter

Fault thrown when moving a standalone host between datacenters, and one or more of the virtual machines registered on the host are already registered to hosts in the target datacenter.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**hostname** | **str** | Name of the target host.  ***Since:*** vSphere API 4.0  | 
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Virtual machines in the target datacenter which have the same registration information as those belonging to the target host.  ***Since:*** vSphere API 4.0  Refers instances of *VirtualMachine*.  | 

## Example

```python
from vmware_vi.models.vm_already_exists_in_datacenter import VmAlreadyExistsInDatacenter

# TODO update the JSON string below
json = "{}"
# create an instance of VmAlreadyExistsInDatacenter from a JSON string
vm_already_exists_in_datacenter_instance = VmAlreadyExistsInDatacenter.from_json(json)
# print the JSON string representation of the object
print VmAlreadyExistsInDatacenter.to_json()

# convert the object into a dict
vm_already_exists_in_datacenter_dict = vm_already_exists_in_datacenter_instance.to_dict()
# create an instance of VmAlreadyExistsInDatacenter from a dict
vm_already_exists_in_datacenter_form_dict = vm_already_exists_in_datacenter.from_dict(vm_already_exists_in_datacenter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


