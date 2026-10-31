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
  A build information type is a grouping of characteristics that describe how a particular version of software was converted from source code to executable code.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BuildInformationType extends UcoInherentCharacterizationThing {

  private Configuration buildConfiguration;
  private String buildID;
  private String buildLabel;
  private String buildOutputLog;
  private String buildProject;
  private String buildScript;
  private BuildUtilityType buildUtility;
  private String buildVersion;
  private ZonedDateTime compilationDate;
  private List<CompilerType> compilers;
  private List<LibraryType> libraries;


}