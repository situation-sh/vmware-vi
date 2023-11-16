# UserInputRequiredParameterMetadata

The *UserInputRequiredParameterMetadata* data object represents policy option metadata information for configuration data.  The Profile Engine saves configuration data from the user input options in the host *AnswerFile*. See the *HostProfile.ExecuteHostProfile* and *HostProfileManager.ApplyHostConfig_Task* methods.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input_parameter** | [**List[ProfileParameterMetadata]**](ProfileParameterMetadata.md) | Metadata for user input options.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.user_input_required_parameter_metadata import UserInputRequiredParameterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UserInputRequiredParameterMetadata from a JSON string
user_input_required_parameter_metadata_instance = UserInputRequiredParameterMetadata.from_json(json)
# print the JSON string representation of the object
print UserInputRequiredParameterMetadata.to_json()

# convert the object into a dict
user_input_required_parameter_metadata_dict = user_input_required_parameter_metadata_instance.to_dict()
# create an instance of UserInputRequiredParameterMetadata from a dict
user_input_required_parameter_metadata_form_dict = user_input_required_parameter_metadata.from_dict(user_input_required_parameter_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


