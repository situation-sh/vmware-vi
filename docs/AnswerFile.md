# AnswerFile

The *AnswerFile* data object contains host-specific information that a host will use in combination with a *HostProfile* for configuration.  Answer files are stored on the vCenter Server, along with host profiles. An answer file is always associated with a particular host.  To supply host-specific data: - Specify deferred parameters when you call the   *HostProfile*.*HostProfile.ExecuteHostProfile*   method. The host profile engine will verify the set of parameters for the   additional configuration data. - Use the complete required input list   (*ProfileExecuteResult*.*ProfileExecuteResult.requireInput*\\[\\])   as user input for the   *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task*   method. When you apply the profile, the vCenter Server saves the additional configuration   data in the *AnswerFile.userInput* list. - Use the *HostProfileManager*.*HostProfileManager.UpdateAnswerFile_Task* method. This method will update an existing answer file or create a new one.    ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input** | [**List[ProfileDeferredPolicyOptionParameter]**](ProfileDeferredPolicyOptionParameter.md) | List containing host-specific configuration data.  ***Since:*** vSphere API 5.0  | [optional] 
**created_time** | **datetime** | Time at which the answer file was created.  ***Since:*** vSphere API 5.0  | 
**modified_time** | **datetime** | Time at which the answer file was last modified.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.answer_file import AnswerFile

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerFile from a JSON string
answer_file_instance = AnswerFile.from_json(json)
# print the JSON string representation of the object
print AnswerFile.to_json()

# convert the object into a dict
answer_file_dict = answer_file_instance.to_dict()
# create an instance of AnswerFile from a dict
answer_file_form_dict = answer_file.from_dict(answer_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


