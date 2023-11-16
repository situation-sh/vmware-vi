# ProfileMetadataProfileOperationMessage

Some operations on host profile documents may cause unexpected result.  For example, deleting a profile instance of vswitch may break the network connectivity. This data class provides the localizable message which may be presented before or after an operation happens.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_name** | **str** | The operation name.  ***Since:*** vSphere API 6.7  | 
**message** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.profile_metadata_profile_operation_message import ProfileMetadataProfileOperationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetadataProfileOperationMessage from a JSON string
profile_metadata_profile_operation_message_instance = ProfileMetadataProfileOperationMessage.from_json(json)
# print the JSON string representation of the object
print ProfileMetadataProfileOperationMessage.to_json()

# convert the object into a dict
profile_metadata_profile_operation_message_dict = profile_metadata_profile_operation_message_instance.to_dict()
# create an instance of ProfileMetadataProfileOperationMessage from a dict
profile_metadata_profile_operation_message_form_dict = profile_metadata_profile_operation_message.from_dict(profile_metadata_profile_operation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


