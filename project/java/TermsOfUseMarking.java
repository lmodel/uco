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
  A terms of use marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual statement specifying the Terms of Use (that is, the conditions under which the content may be shared, applied, or otherwise used) of the marked content. An example of this would be used to communicate a simple statement, such as 'Acme Inc. is not responsible for the content of this file'.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TermsOfUseMarking extends MarkingModel {

  private List<String> definitionType;
  private String termsOfUse;


}