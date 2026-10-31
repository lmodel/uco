package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A Windows registry key facet is a grouping of characteristics unique to a particular key within a Windows registry (A hierarchical database that stores low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsRegistryKeyFacet extends Facet {

  private Integer numberOfSubkeys;
  private ObservableObject observableCreator;
  private String observableKey;
  private ZonedDateTime observableModifiedTime;
  private List<WindowsRegistryValue> registryValues;


}