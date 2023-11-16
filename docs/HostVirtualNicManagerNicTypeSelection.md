# HostVirtualNicManagerNicTypeSelection

DataObject which lets a VirtualNic be marked for use as a *HostVirtualNicManagerNicType_enum*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic** | [**HostVirtualNicConnection**](HostVirtualNicConnection.md) |  | 
**nic_type** | **List[str]** |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic_manager_nic_type_selection import HostVirtualNicManagerNicTypeSelection

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicManagerNicTypeSelection from a JSON string
host_virtual_nic_manager_nic_type_selection_instance = HostVirtualNicManagerNicTypeSelection.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicManagerNicTypeSelection.to_json()

# convert the object into a dict
host_virtual_nic_manager_nic_type_selection_dict = host_virtual_nic_manager_nic_type_selection_instance.to_dict()
# create an instance of HostVirtualNicManagerNicTypeSelection from a dict
host_virtual_nic_manager_nic_type_selection_form_dict = host_virtual_nic_manager_nic_type_selection.from_dict(host_virtual_nic_manager_nic_type_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


