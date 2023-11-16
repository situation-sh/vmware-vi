# HostBIOSInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bios_version** | **str** | The current BIOS version of the physical chassis  ***Since:*** VI API 2.5  | [optional] 
**release_date** | **datetime** | The release date for the BIOS.  ***Since:*** VI API 2.5  | [optional] 
**vendor** | **str** | The vendor for the BIOS.  ***Since:*** vSphere API 6.5  | [optional] 
**major_release** | **int** | BIOS Major Release  ***Since:*** vSphere API 6.5  | [optional] 
**minor_release** | **int** | \&quot;BIOS Minor Release  ***Since:*** vSphere API 6.5  | [optional] 
**firmware_major_release** | **int** |  | [optional] 
**firmware_minor_release** | **int** | Embedded Controller Firmware Minor Release  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_bios_info import HostBIOSInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostBIOSInfo from a JSON string
host_bios_info_instance = HostBIOSInfo.from_json(json)
# print the JSON string representation of the object
print HostBIOSInfo.to_json()

# convert the object into a dict
host_bios_info_dict = host_bios_info_instance.to_dict()
# create an instance of HostBIOSInfo from a dict
host_bios_info_form_dict = host_bios_info.from_dict(host_bios_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


