# CustomizationLinuxPrep

This is the Linux counterpart to the Windows Sysprep object.  LinuxPrep contains machine-wide settings that identify a Linux machine in the same way that the Sysprep type identifies a Windows machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | [**CustomizationName**](CustomizationName.md) |  | 
**domain** | **str** | The fully qualified domain name.  | 
**time_zone** | **str** | The case-sensitive timezone, such as Europe/Sofia.  &lt;a href&#x3D;\&quot;timezone.html\&quot;title&#x3D;\&quot;Display list of Valid timeZone values...\&quot;&gt; **Valid timeZone values**&lt;/a&gt; are based on the tz (timezone) database used by Linux and other Unix systems. The values are strings (xsd:string) in the form \&quot;Area/Location,\&quot; in which Area is a continent or ocean name, and Location is the city, island, or other regional designation.  See the &lt;a href&#x3D;\&quot;https://kb.vmware.com/selfservice/microsites/search.do?language&#x3D;en_US&amp;cmd&#x3D;displayKC&amp;externalId&#x3D;2145518\&quot;target&#x3D;\&quot;_blank\&quot;&gt;List of supported time zones for different vSphere versions in Linux/Unix systems&lt;/a&gt;.  ***Since:*** vSphere API 4.0  | [optional] 
**hw_clock_utc** | **bool** | Specifies whether the hardware clock is in UTC or local time. - True when the hardware clock is in UTC. - False when the hardware clock is in local time.    ***Since:*** vSphere API 4.0  | [optional] 
**script_text** | **str** | The script to run before and after GOS customization.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.customization_linux_prep import CustomizationLinuxPrep

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationLinuxPrep from a JSON string
customization_linux_prep_instance = CustomizationLinuxPrep.from_json(json)
# print the JSON string representation of the object
print CustomizationLinuxPrep.to_json()

# convert the object into a dict
customization_linux_prep_dict = customization_linux_prep_instance.to_dict()
# create an instance of CustomizationLinuxPrep from a dict
customization_linux_prep_form_dict = customization_linux_prep.from_dict(customization_linux_prep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


