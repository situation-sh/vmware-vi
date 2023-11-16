# HostSystemInfo

Information about the system as a whole. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** | Hardware vendor identification.  | 
**model** | **str** | System model identification.  | 
**uuid** | **str** | Hardware BIOS identification.  | 
**other_identifying_info** | [**List[HostSystemIdentificationInfo]**](HostSystemIdentificationInfo.md) | Other System identification information.  This information may be vendor specific  ***Since:*** VI API 2.5  | [optional] 
**serial_number** | **str** |  | [optional] 
**qualified_name** | [**List[HostQualifiedName]**](HostQualifiedName.md) | List of qualified names used to identify the host in a specific context.  Unlike the other types of system identification information, these can potentially change as a result of configuration.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**vvol_host_nqn** | [**HostQualifiedName**](HostQualifiedName.md) |  | [optional] 
**vvol_host_id** | **str** | Host id used by Vvol.  The hostd id, obtained through vmkctl storage control path while fetching the NVMe info.  | [optional] 

## Example

```python
from vmware_vi.models.host_system_info import HostSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemInfo from a JSON string
host_system_info_instance = HostSystemInfo.from_json(json)
# print the JSON string representation of the object
print HostSystemInfo.to_json()

# convert the object into a dict
host_system_info_dict = host_system_info_instance.to_dict()
# create an instance of HostSystemInfo from a dict
host_system_info_form_dict = host_system_info.from_dict(host_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


