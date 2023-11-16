# VirtualMachineConfigOptionDescriptor

Contains the definition of a unique key that can be used to retrieve a configOption object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key used to identify a configOption object in this *EnvironmentBrowser*.  | 
**description** | **str** | A description of the configOption object.  | [optional] 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of hosts to which this descriptor applies.  List of hosts is not set when descriptor is returned from *Datacenter.queryDatacenterConfigOptionDescriptor*.  Refers instances of *HostSystem*.  | [optional] 
**create_supported** | **bool** | Indicates whether the associated set of configuration options can be used for virtual machine creation on a given host or cluster.  ***Since:*** vSphere API 4.0  | 
**default_config_option** | **bool** | Indicates whether the associated set of virtual machine configuration options is the default one for a given host or cluster.  Latest version is marked as default unless other version is specified via *ComputeResourceConfigInfo.defaultHardwareVersionKey* or *DatacenterConfigInfo.defaultHardwareVersionKey*. If this setting is TRUE, virtual machine creates will use the associated set of configuration options, unless a config version is explicitly specified in the *ConfigSpec*.  ***Since:*** vSphere API 4.0  | 
**run_supported** | **bool** | Indicates whether the associated set of configuration options can be used to power on a virtual machine on a given host or cluster.  ***Since:*** vSphere API 5.1  | 
**upgrade_supported** | **bool** | Indicates whether the associated set of configuration options can be used as a virtual hardware upgrade target.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_machine_config_option_descriptor import VirtualMachineConfigOptionDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConfigOptionDescriptor from a JSON string
virtual_machine_config_option_descriptor_instance = VirtualMachineConfigOptionDescriptor.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConfigOptionDescriptor.to_json()

# convert the object into a dict
virtual_machine_config_option_descriptor_dict = virtual_machine_config_option_descriptor_instance.to_dict()
# create an instance of VirtualMachineConfigOptionDescriptor from a dict
virtual_machine_config_option_descriptor_form_dict = virtual_machine_config_option_descriptor.from_dict(virtual_machine_config_option_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


