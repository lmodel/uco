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
  A Windows computer specification facet is a grouping of characteristics unique to the hardware and software of a programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating system. [based on merriam-webster.com/dictionary/computer]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsComputerSpecificationFacet extends Facet {

  private List<String> domain;
  private List<GlobalFlagType> globalFlagList;
  private ZonedDateTime lastShutdownDate;
  private String msProductID;
  private String msProductName;
  private String netBIOSName;
  private ZonedDateTime osInstallDate;
  private ZonedDateTime osLastUpgradeDate;
  private Identity registeredOrganization;
  private Identity registeredOwner;
  private ObservableObject windowsDirectory;
  private ObservableObject windowsSystemDirectory;
  private ObservableObject windowsTempDirectory;


}