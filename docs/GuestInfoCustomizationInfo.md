# GuestInfoCustomizationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customization_status** | **str** | The customization status for this VM  See also *GuestInfoCustomizationStatus_enum*for the list of supported values.  ***Since:*** vSphere API 7.0.2.0  | 
**start_time** | **datetime** | The time when the customization process has started inside the guest OS  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**end_time** | **datetime** | The time when the customization process has completed inside the guest OS  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**error_msg** | **str** | Description of the error if there is error for the customization process inside the guest OS  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_info_customization_info import GuestInfoCustomizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestInfoCustomizationInfo from a JSON string
guest_info_customization_info_instance = GuestInfoCustomizationInfo.from_json(json)
# print the JSON string representation of the object
print GuestInfoCustomizationInfo.to_json()

# convert the object into a dict
guest_info_customization_info_dict = guest_info_customization_info_instance.to_dict()
# create an instance of GuestInfoCustomizationInfo from a dict
guest_info_customization_info_form_dict = guest_info_customization_info.from_dict(guest_info_customization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


