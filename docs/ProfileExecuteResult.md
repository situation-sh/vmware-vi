# ProfileExecuteResult

The *ProfileExecuteResult* data object contains the results from a *HostProfile*.*HostProfile.ExecuteHostProfile* operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the profile execution operation.  The value is a string that contains one of the *ProfileExecuteResultStatus_enum* enumerations.  ***Since:*** vSphere API 4.0  | 
**config_spec** | [**HostConfigSpec**](HostConfigSpec.md) |  | [optional] 
**inapplicable_path** | **List[str]** | List of property paths.  Each path identifies a policy that does not apply to this host. For example, if the precheck policies for a port group are not satisfied, the port group will not be created when you apply the profile to the host. Based on this information, the client might not display that part of the profile tree.  ***Since:*** vSphere API 4.0  | [optional] 
**require_input** | [**List[ProfileDeferredPolicyOptionParameter]**](ProfileDeferredPolicyOptionParameter.md) | List that describes the required input for host configuration and identifies any policy options that still require parameter data.  Each entry in the list specifies the path to a policy and a parameter list. If the call to *HostProfile.ExecuteHostProfile* includes deferred parameters, the &lt;code&gt;requireInput&lt;/code&gt; entries (&lt;code&gt;requireInput\\[\\].&lt;/code&gt;*ProfileDeferredPolicyOptionParameter.parameter*\\[\\]) will be populated with the parameter data that was passed to the execute method. For policies that still require input data, the parameter list in the corresponding entry will be null.  A vSphere client that displays a GUI can use this information to show the host-specific configuration policy options. The client can highlight required input fields and ask the user for data in increments instead of collecting all of the input at once. For example, in the first pass, the client collects a minimum of user input and sends that to the Server. The Server evaluates the profile and might decide to invalidate a particular part of the subtree or enable a new subtree in the profile. This would result in a new set of invalid paths (*ProfileExecuteResult.inapplicablePath*\\[\\]) and required input property paths (*ProfileDeferredPolicyOptionParameter*.*ProfileDeferredPolicyOptionParameter.inputPath*). The client can make a series of calls to the method until it achieves a success status.  When *HostProfile.ExecuteHostProfile* returns a success status, the &lt;code&gt;requireInput&lt;/code&gt; list contains the complete list of parameters, consisting of the following data: - Deferred parameter values resolved through successive calls to   *HostProfile.ExecuteHostProfile*. - Default parameter values from the host configuration. - User-specified values that override the defaults.    You can specify the returned &lt;code&gt;requireInput&lt;/code&gt; list in the &lt;code&gt;userInput&lt;/code&gt; parameter to the *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task* method. The Server will use the list to update the *AnswerFile* associated with the host.  ***Since:*** vSphere API 4.0  | [optional] 
**error** | [**List[ProfileExecuteError]**](ProfileExecuteError.md) | List of errors that were encountered during execute.  This field will be set if status is set to error.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_execute_result import ProfileExecuteResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileExecuteResult from a JSON string
profile_execute_result_instance = ProfileExecuteResult.from_json(json)
# print the JSON string representation of the object
print ProfileExecuteResult.to_json()

# convert the object into a dict
profile_execute_result_dict = profile_execute_result_instance.to_dict()
# create an instance of ProfileExecuteResult from a dict
profile_execute_result_form_dict = profile_execute_result.from_dict(profile_execute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


