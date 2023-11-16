# GuestInfoNamespaceGenerationInfo

A data class for the namespace and its corresponding generation number The generation number can be used to track updates to the corresponding namespace.  An update to the generation number indicates that the return value of *VirtualMachineNamespaceManager.FetchEventsFromGuest* may have changed.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The namespace name as the unique key.  ***Since:*** vSphere API 5.1  | 
**generation_no** | **int** | Namespace generation number.  Generation number is changed whenever there is new unread event pending from the guest to the VMODL.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.guest_info_namespace_generation_info import GuestInfoNamespaceGenerationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestInfoNamespaceGenerationInfo from a JSON string
guest_info_namespace_generation_info_instance = GuestInfoNamespaceGenerationInfo.from_json(json)
# print the JSON string representation of the object
print GuestInfoNamespaceGenerationInfo.to_json()

# convert the object into a dict
guest_info_namespace_generation_info_dict = guest_info_namespace_generation_info_instance.to_dict()
# create an instance of GuestInfoNamespaceGenerationInfo from a dict
guest_info_namespace_generation_info_form_dict = guest_info_namespace_generation_info.from_dict(guest_info_namespace_generation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


