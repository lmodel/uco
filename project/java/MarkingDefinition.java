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
  A marking definition is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MarkingDefinition extends MarkingDefinitionAbstraction {

  private List<MarkingModel> definition;
  private String definitionType;


}