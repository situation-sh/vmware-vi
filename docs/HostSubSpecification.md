# HostSubSpecification

Host sub specification data are the data used when create a virtual device, and/or configure the virtual device and its related host services.  A typical example of host sub specification data is the DVS host view specification, which is used when create DVS host view on an ESXi host and configure the virtual switch on the host. The introduction of this type of data is for improving the availability of the ESXi host management. For example, when the VirtualCenter server is not available, an ESXi host will have enough information to reconfigure DVS host view properly when the ESXi host is booted from stateless or stateless caching. Host sub specification data are data for VMware internal data structure used in virtual device creation and configuration. They are different to *AnswerFile* which are from public knowledge domain or the public API of VMware ESXi host services. When the host sub specification data for a single feature are stored in multiple host sub specification data objects, it is the responsibility of the host specification source in this feature to guarantee the completeness and consistency of these host sub specification objects.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The full name of the host sub specification.  The format of this member variable is: CompanyName\\_ProductName\\_SubSpecName. Thus, name conflict is avoided by containing the &lt;code&gt;company name&lt;/code&gt;, &lt;code&gt;product name&lt;/code&gt;, and &lt;code&gt; sub specification name&lt;/code&gt; in this full name.  ***Since:*** vSphere API 6.5  | 
**created_time** | **datetime** | Time at which the host sub specification was created.  ***Since:*** vSphere API 6.5  | 
**data** | **List[int]** | The host sub specification data  ***Since:*** vSphere API 6.5  | [optional] 
**binary_data** | **bytearray** | The host sub specification data in Binary for wire efficiency.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.host_sub_specification import HostSubSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of HostSubSpecification from a JSON string
host_sub_specification_instance = HostSubSpecification.from_json(json)
# print the JSON string representation of the object
print HostSubSpecification.to_json()

# convert the object into a dict
host_sub_specification_dict = host_sub_specification_instance.to_dict()
# create an instance of HostSubSpecification from a dict
host_sub_specification_form_dict = host_sub_specification.from_dict(host_sub_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


