# ApplyHostProfileConfigurationSpec

The data object that contains the objects needed to remediate a host in host profile batch apply.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**task_list_requirement** | **List[str]** | The task requirements from the results of *HostProfileManager.GenerateConfigTaskList* method  ***Since:*** vSphere API 6.5  | [optional] 
**task_description** | [**List[LocalizableMessage]**](LocalizableMessage.md) | Description of tasks that will be performed on the host to carry out HostProfile application.  ***Since:*** vSphere API 6.5  | [optional] 
**reboot_stateless** | **bool** | For a stateless host, there are two approaches to apply a host profile: (1) Reboot the host and apply the host profile at boot time.  (2) Apply the host profile directly from VC. We call this as regular apply. The variable rebootStateless allows users to choose the first approach from the two approaches above: apply host profile by rebooting this host.  ***Since:*** vSphere API 6.5  | [optional] 
**reboot_host** | **bool** | For regular apply, when some of the tasks requires reboot, that this variable is&lt;code&gt;true&lt;/code&gt; indicates that the reboot automatically happens in the batch profile apply than that the user will manually reboot the system later.  For stateless host, this variable takes effect only when the variable &lt;code&gt;rebootStateless&lt;/code&gt; above is &lt;code&gt;false&lt;/code&gt;.  ***Since:*** vSphere API 6.5  | [optional] 
**fault_data** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.apply_host_profile_configuration_spec import ApplyHostProfileConfigurationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyHostProfileConfigurationSpec from a JSON string
apply_host_profile_configuration_spec_instance = ApplyHostProfileConfigurationSpec.from_json(json)
# print the JSON string representation of the object
print ApplyHostProfileConfigurationSpec.to_json()

# convert the object into a dict
apply_host_profile_configuration_spec_dict = apply_host_profile_configuration_spec_instance.to_dict()
# create an instance of ApplyHostProfileConfigurationSpec from a dict
apply_host_profile_configuration_spec_form_dict = apply_host_profile_configuration_spec.from_dict(apply_host_profile_configuration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


